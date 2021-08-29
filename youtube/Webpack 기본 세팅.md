# Webpack 기본 세팅

[참고 영상](https://www.youtube.com/watch?v=zal9HVgrMaQ)

## Webpack?

다양한 모듈들을 하나의 js파일로 만들어주는 것이다.

1. npm init

   ```bash
   npm init
   ```

2. 이러면 패키지 json이 생김

3. npm install

   ```bash
   npm install webpack webpack-cli --save-dev
   ```

   install => i, --save-dev => -D (개발용 설치) 로 축약 가능

4. webpack.config.js 라는 설정을 위한 파일 생성

   웹팩 명령어를 실행했을때 자동으로 설정시켜주는 도움을 줌

   [webpack.config.js 설명](https://www.daleseo.com/webpack-config/)

5. 웹팩 설정

   ```javascript
   const path = require('path');
   
   module.exports = {
       entry: './src/index.js',
       output: {
           filename: 'main.js',
           path: path.resolve(__dirname,'dist')
       }
   }
   ```

6. pack.json에 scripts 내부에 `'build': 'webpack'`을 추가해준다. (그러면 npm run build가 가능해짐)

여기까지 진행하면 빌드시에 dist안에 js파일만 있다! 우리는 html파일도 필요하다 `npm -i html-webpack-plugin`을 이용해서 필요한 모듈을 설치하자. 그리고 webpack.config.js를 조금 더 수정해보자

```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    entry: './src/index.js',
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname,'dist')
    },
    plugins: [new HtmlWebpackPlugin({
        template: './index.html',
    })],
}
```

해당 모듈의 도움으로 js,html파일 둘다 생길 것이다! 그런데 이경우에 html파일을 실행시키면 잘 되긴 하지만 우리가 필요한 작업을 수행하고 저장할때마다 다시 빌드를 해줘야 적용이 된다는 문제가 생긴다.

이럴때 사용하는 것이 webpack-dev-server가 있다 `npm i webpack-dev-server -D` 이런 식으로 설치하고 아래와 같이 설정을 해줘야 한다.

```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    entry: './src/index.js',
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname,'dist')
    },
    plugins: [new HtmlWebpackPlugin({
        template: './index.html',
    })],
    devServer: {
        static: {
            directory: path.resolve(__dirname, 'dist')
        },
        port: 8080,
    }
}
```

그리고 package.json에서 scripts안에 `"start": "webpakc serve --open --mode=development"`을 작성해둔다. 그리고 npm start, npm run start를 이용하면 데브서버를 띄워둘 수가 있다. 그리고 build에도 --mode=production을 추가시켜줘야 한다.

## css도 추가하자

`npm i -D style-loader css-loader` 를 설치하고 또 세팅해줄 수 있도록 하자.

```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    entry: './src/index.js',
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname,'dist')
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ["style-loader","css-loader"], // 역순으로 실행시킨다. 즉, css => style순서
            }
        ]
    },
    plugins: [new HtmlWebpackPlugin({
        template: './index.html',
    })],
    devServer: {
        static: {
            directory: path.resolve(__dirname, 'dist')
        },
        port: 8080,
    }
}
```

위 방식으로 상태를 보면 인라인에 스타일을 추가한듯이 되어있다. 우리는 외부에서 파일을 가져오는 것을 더 선호한다. 그렇다면 한번 보자 일단. `npm i -D mini-css-extract-plugin`을 이용해 설치하자. 그리고 플로그인을 수정하자

```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: './src/index.js',
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname,'dist')
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [MiniCssExtractPlugin.loader,"css-loader"],
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
        	template: './index.html',
    	}),
        new MiniCssExtractPlugin({
            filename: "common.css",
        })
    ],
    devServer: {
        static: {
            directory: path.resolve(__dirname, 'dist')
        },
        port: 8080,
    }
}
```

이렇게 하면 외부 css파일을 가져오는 형식으로 하는 것을 확인할 수가 있다. 

## 외부 파일

외부 파일을 가져오는 경우도 많을 것이다. 대표적으로 이미지가 그렇지 않은가? 일단 설치를 진행해보자. `npm i -D file-loader` 그리고 html파일에 넣어줄 js파일에서 이미지를 import해오자. 그리고 설정을 하자.

```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: './src/index.js',
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname,'dist')
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [MiniCssExtractPlugin.loader,"css-loader"],
            },
            {
                test: /\.jpg$/,
                use: ["file-loader"]
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
        	template: './index.html',
    	}),
        new MiniCssExtractPlugin({
            filename: "common.css",
        })
    ],
    devServer: {
        static: {
            directory: path.resolve(__dirname, 'dist')
        },
        port: 8080,
    }
}
```

그러면 에러 없이 이미지를 성공적으로 가져오는 것을 볼 수가 있을 것이다.

## 클린빌드

자주 막 돌리다보면 이전 빌드때문에 남아있는 찌꺼기 파일이 있는 경우도 있다. 이런 경우에 이걸 없애주는 것이 용량에 도움이 될것이다. 그럴 경우 도움되는 모듈이 있다. `npm i -D clean-webpack-plugin`을 이용해 설치하고 추가해보자.

```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

module.exports = {
    entry: './src/index.js',
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname,'dist')
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [MiniCssExtractPlugin.loader,"css-loader"],
            },
            {
                test: /\.jpg$/,
                use: ["file-loader"]
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
        	template: './index.html',
    	}),
        new MiniCssExtractPlugin({
            filename: "common.css",
        }),
        new CleanWebpackPlugin()
    ],
    devServer: {
        static: {
            directory: path.resolve(__dirname, 'dist')
        },
        port: 8080,
    }
}
```

