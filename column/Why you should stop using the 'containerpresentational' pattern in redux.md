# Why you should stop using the 'container/presentational' pattern in redux

[컬럼 링크](https://medium.com/nmc-techblog/why-you-should-stop-using-the-container-presentational-pattern-in-redux-29b112406128)  [레딧 코멘트 링크](https://www.reddit.com/r/reactjs/comments/ox6cwk/why_you_should_stop_using_the/)

> 리덕스 스타일 가이드는 중요한 룰이 있다. '스토어에서 데이터를 읽기 위해 더 많은 컴포넌트를 연결해라'. 과거의 예시를 통해 이 룰이 중요한 성능적 향상에 대한 기대가 있는 것을 살펴보자.

'container/presentational' 패턴은 리덕스나 다른 스토어 메니지먼트 패키지를 이용할 때 최고의 실천방식이었다. [Dan Abramov](https://twitter.com/dan_abramov) 와 [Michael Chan](https://twitter.com/chantastic) 에 의해 설명되어 왔다. 만약 우리가 짧게 유지 되는 것을 원한다면, 컨테이너는 보통 데이터 fetching 로직과 스토어로의 데이터 접근을 가지고 있다. 다른 손에는, presentational컴포넌트는 좀 더 제네릭하고 props로써 데이터를 대표할 뿐이다. 이 패턴은 리액트 훅이 설명되어지기 전까진 일반적이었고 아마 모든 클래스로 리액트를 이용하던 모든 개발자가 보았거나 사용하고 있었다.

하지만 훅의 세계에서, 이 접근법은 치명적인 성능 문제를 낳을 수도 있다. 게다가, [Redux best practices](https://redux.js.org/style-guide/style-guide#connect-more-components-to-read-data-from-the-store) 는 이제 우리가 스토어에 직접다가가 읽는 컴포넌트를 연결하라고 제안한다. 도당체 무슨일이 있었길래?

## 우리의 예시 앱

왼쪽 사이드바에는 포켓몬들의 목록이, 오른쪽 박스에는 선택된 포켓몬이 보여지는 앱을 만들었다고 하자. 왼쪽 사이드바에서 포켓몬 이름을 선택하면 오른쪽 그림이 바뀔 것이다. 

이 첫 접근에 의하면, 나는 컨테이너 위에 커넥트를 사용하겠다고 결심하고, 스토어로부터 모든 데이터를 쿼리하고 디스패치할 것이다.

나는 프랍스를 사용하는 내 컴포넌트로 데이터를 넘길 것이다.

```react
export const PokemonsPage = ({
 asyncGetAllPokemons,
 asyncGetPokemonDetails,
 setSelectedPokemon,
 pokemons,
 selectedPokemonId,
 selectedPokemon
}) => {
 return (
   <PokemonsPageWrapper>
     <PokemonsSidebar
       asyncGetAllPokemons={asyncGetAllPokemons}
       pokemons={pokemons}
       setSelectedPokemon={setSelectedPokemon}
     />
     <PokemonView
       selectedPokemonId={selectedPokemonId}
       asyncGetPokemonDetails={asyncGetPokemonDetails}
       selectedPokemon={selectedPokemon}
     />
   </PokemonsPageWrapper>
)
}

export default connect(
({ pokemons }) => ({
   pokemons: pokemons.data,
   selectedPokemonId: pokemons.selectedPokemonId,
   selectedPokemon: pokemons.selectedPokemonData
}),
{
   asyncGetAllPokemons,
   setSelectedPokemon,
   asyncGetPokemonDetails
}
)(PokemonsPage)
```

컴포넌트들은 단지 data를 fetch하고 props를 베이스로해서 보여주고 있다. React proiler를 열고 기록을 해보기로 했다.

그러니 어떤 일이 일어나는가? 왼쪽 사이드바의 포켓몬 이름을 클릭할 때, 두개의 랜더를 실행시킨다! 우선적으로 우리가 보는 것은 `PokemonsSidebar` 가 랜더링되고 1ms정도 걸린다는 것이다. 하지만, 왜 그런거지? 변한게 있는게 아닌데 렌더링이 되고 있다! 그것은 리덕스 스토어 안의 변화가 원인이 되어 부모 컴포넌트가 랜더링 되기 때문이며 자식 컴포넌트또한 부모에 의해 랜더링이 다시 된다. 우리는 또한 `render duration` 이 13.6ms걸리고 `PokemonsSidebar`에 의해 재 랜더링 되는 것을 볼 수 있다.

두번째 접근법으로, `useSelector` `useDispatch` 를 통해 코드를 리팩토링 해보기로 했다. 코드는 아래와 같다

```react
export const PokemonView = () => {
 const selectedPokemonId = useSelector(
  ({ pokemons }) => pokemons.selectedPokemonId
)
 const selectedPokemon = useSelector(
  ({ pokemons }) => pokemons.selectedPokemonData
)
 const dispatch = useDispatch()

 useEffect(() => {
   if (selectedPokemonId) {
     dispatch(asyncGetPokemonDetails(selectedPokemonId))
  }
}, [selectedPokemonId, dispatch])

 return (
     <PokemonCard>
      {selectedPokemon && (
         <SmallImage
           src={`https://pokeres.bastionbot.org/images/pokemon/${selectedPokemon.id}.png`}
           alt={selectedPokemon.name}
         />
      )}
       <div>{selectedPokemon?.name}</div>
     </PokemonCard>
)
}
export const PokemonsSidebar = () => {
 const pokemons = useSelector(({ pokemons }) => pokemons.data)
 const [pokemonsNumber, setPokemonsNumber] = useState(10)
 const dispatch = useDispatch()
 useEffect(() => {
   dispatch(asyncGetAllPokemons(pokemonsNumber))
}, [dispatch, pokemonsNumber])
 return (
   <SidebarWrapper>
     <PokemonsNumberDropdown setPokemonsNumber={setPokemonsNumber} pokemonsNumber={pokemonsNumber} />
     <ul>
      {pokemons.map((pokemon) => (
         <PokemonItem
           key={pokemon.name}
           onClick={() => {
             dispatch(setSelectedPokemon(pokemon))
          }}
         >
          {pokemon.name}
         </PokemonItem>
      ))}
     </ul>
   </SidebarWrapper>
)
}
```

해당 코드를 profiler를 통해서 확인 해보자. 그러면 `PokemonsSidebar` 가 더이상 리랜더링되지 않는 것을 확인 할 수 있고 랜더 시간또한 매우 짧아지는 것을 확인할 수가 있다.

## 왜 이런 현상이?

함수 컴포넌트들을 사용해왔던 시절부터, 부모 컴포넌트가 랜더링되면 **모든트리가 같이 랜더링이 되어왔다.** 우리의 함수 컴포넌트가 래핑되어있지 않다면, 그들은 자동적으로 재랜더링 될 것이다 심지어 props나 상태가 변화하지 않아도. 우리는 성능에 대한 주목을 조금은 더 할 필요가 있다.

## 조금 생각해볼 점

마지막 색션으로부터 이해해본다면, 이것은 리덕스만의 문제는 아니다. 'container/presentational' 패턴은 여전히 괜찮은 솔루션이다. 단지 컴포넌트간의 문제를 살펴봐야하는 것이다