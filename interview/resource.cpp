class Resource {
    public:
    Resource() {handle = openResource();}
    -Resource() {closeResource( handel );}
    ResourceHandle getHandel() { return handle; }
    private:
    ResourceHandle handle;
    Resource ( Resource const & ); // 비공개 복사 생성자
    Resource & operator = (Resource const & ); // 비공개 대입 연산자
}