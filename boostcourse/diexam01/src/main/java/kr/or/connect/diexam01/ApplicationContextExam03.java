package kr.or.connect.diexam01;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class ApplicationContextExam03 {

	public static void main(String[] args) {
		ApplicationContext ac = new AnnotationConfigApplicationContext(ApplicationConfig.class);
		   
		Car car = (Car)ac.getBean("car"); //Car.class 를 "car"대신 적어줘도 실행이 된다. 해당 클레스 타입을 찾아가는 형식이라 그렇다
		car.run();
		
	}
}