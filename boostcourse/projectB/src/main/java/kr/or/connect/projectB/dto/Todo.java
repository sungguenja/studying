package kr.or.connect.projectB.dto;
import java.util.Date;

public class Todo {
	private Integer todoId;
	private String title;
	private String name;
	private Integer sequence;
	private String type;
	private Date regdate;
	
	public Todo(Integer todoId, String title, String name, Integer sequence, String type, Date regdate) {
		super();
		this.todoId = todoId;
		this.title = title;
		this.name = name;
		this.sequence = sequence;
		this.type = type;
		this.regdate = regdate;
	}
	
	public Integer getTodoId() {
		return todoId;
	}
	public void Id(Integer todoId) {
		this.todoId = todoId;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getSequence() {
		return sequence.toString();
	}
	public void setSequence(int sequence) {
		this.sequence = sequence;
	}
	public String gettype() {
		return type;
	}
	public void setTYpe(String type) {
		this.type = type;
	}
	public String getRegDate() {
		return regdate.toString();
	}
	public void setRegDate(Date regdate) {
		this.regdate = regdate;
	}
	@Override
	public String toString() {
		return "todo [todoId="+todoId+", title="+title+", name="+name+", sequence="+sequence+", type="+type+", regdate="+regdate+"]";
	}
}
