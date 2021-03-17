public class java_busy_waitin {
    Object theLock = new Object();
    synchronized( theLock ){
        Thread task = new TheTask( theLock );
        task.start();
        try {
            theLock.wait();
        }
        catch (InterruptedException e) {
            // 인터럽트가 발생하면 필요한 작업을 처리
        }
    }
    // 필요한 상황들 쭉 써두기
    class TheTask extends Thread {
        private Object theLock;
        public TheTask( Object theLock ){
            this.theLock = theLock;
        }
        public void run(){
            synchronized( theLock ){
                // 작업처리
                theLock.notify();
            }
        }
    }
}
