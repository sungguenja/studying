# TCP/IP

[영상 링크](https://youtu.be/BEK354TRgZ8)

> 1. 인터넷 
> 2. TCP/IP 계층
> 3. TCP/IP 흐름
> 4. 신뢰할 수 있는 TCP

## 1. 인터넷

잘 연결되어있슴다!

## 2. TCP/IP 계층

> 인터넷에서 컴퓨터들이 서로 정보를 주고 받는데 쓰이는 프로토콜의 집합

- Application Layer
  - 특정 서비스를 제공하기 위해 애플리케이션끼리 정보를 주고 받을 수 있어요
  - FTP, HTTP, SSH, Telnet, DNS, SMTP
- Transport Layer
  - 송신된 데이터를 수신측 애플리케이션에 확실히 전달하게 해요
  - TCP, UDP, RTP, RTCP
- Internet Layer
  - 수신 측 까지 데이터를 전달하기 위해 사용돼요
  - IP,ARP, ICMP, RARP, OSPF
- network access layer
  - 네트워크에 직접 연결된 기기 간 전송을 할 수 있도록 해요.

## 3. TCP/IP 흐름

주소창에 구글을 쳤을때?

이거 검색해서 보도록

## 4. 신뢰할 수 있는 TCP

TCP는 신뢰할 수 있는 프로토콜입니다

데이터량때문에 http로만 통신하기에는 부족하다. 그리고 많은 흐름때문에 손실될 가능성도 높다.

그리고 흐름제어, 오류제어, 혼잡제어로 TCP는 위와 같은 문제를 잡아줄 수가 있다