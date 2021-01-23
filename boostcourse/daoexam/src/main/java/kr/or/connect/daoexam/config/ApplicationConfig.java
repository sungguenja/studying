package kr.or.connect.daoexam.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Import;
import org.springframework.context.annotation.ComponentScan;

@Configuration
@ComponentScan(basePackages = { "kr.or.connect.daoexam.dao" })
@Import({DBConfig.class})
public class ApplicationConfig {

}
