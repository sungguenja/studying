package kr.or.connect.daoexam.dao;

public class RoleDaoSqls {
	public static final String SELECT_ALL = "SELECT role_id, description FROM role order by role_id";
	
	public static final String UPDATE = "UPDATE role SET description = :description WHERE ROLE_ID = :roleId";
	
	public static final String DELETE = "DELETE FROM role where role_id = :roldId";
	
	public static final String SELECT_BY_ROLE_ID = "SELECT role_id, description FROM role where role_id = :roleId";
}