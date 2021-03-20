// 싱글톤을 써서 간단한 로그용 클래스를 구현함
public class Logger {

    // 싱글톤을 생성하고 저장함
    private static final Logger instance = new Logger();

    // 다른 사람은 아무도 이 클래스를 생성할 수 없도록 함
    private Logger() {

    }

    // 싱글톤 인스턴스 리턴
    public static Logger getInsstance() { return instance; }

    /*
    * 콘솔에 문자열 로그 출력
    * 예: Logger.getInstance().log("thi i a test");
    */
    public void log( String msg ){
        System.out.println( System.currentTimeMillis() + ": " + msg );
    }
}

// 지연 초기화 버전 로거
public class Logger {

    // 싱글톤을 생성하여 저장
    private static Logger instance = null; // final 키워드는 빠짐

    // 다른 사람은 아무도 이 클래스를 생성할 수 없도록 함
    private Logger(){

    }

    // 싱글톤 인스턴스 리턴
    public static Logger getInstance() {
        if (instance == null) {
            instance = new Logger();
        }

        return instance;
    }

    // 콘솔에 문자열 로그 출력
    public void log( String msg ){
        System.out.println( System.currentTimeMillis() + ": " + msg );
    }
}