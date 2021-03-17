public class java_busy_wait_notify{
    Thread task = new TheTask();
    synchronized( task ){
        task.start();
        try {
            task.wait();
        }
        catch( InterruptedException e ){
            // 인터럽티드 발생시 실행시킬 코드
        }
    }
    // 하고 싶은 논리 전개
    class TheTask extends Thread{
        public void run(){
            synchronized( this ){
                // 작업 처리
                this.notify();
            }
        }
    }
}