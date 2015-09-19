import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
	
	int numberOfVertices;
	int numberOfEdges;
	int numberOfEvenComponents = -1;
	List<Vertex> tree = new ArrayList<Vertex>();

    public static void main(String[] args) {
    	Solution solution = new Solution();
    	solution.collectInput();
    	solution.dfs(solution.tree.get(0));
    	solution.findNumberOfEvenComponents(solution.tree.get(0));
    	System.out.println(solution.numberOfEvenComponents);
    }
    
    private void findNumberOfEvenComponents(Vertex v) {
    	if(v.childNodes % 2 == 0) {
    		numberOfEvenComponents++;
	    	for(Vertex adj: v.getAdjacencyList()) {
				if(!isAdjParentOfV(v, adj)) {
					findNumberOfEvenComponents(adj);
				}
			}
    	}	
	}

	private int dfs(Vertex v) {
    	if(!v.visited) {
    		v.visited = true;
    		for(Vertex adj: v.getAdjacencyList()) {
    			if(!isAdjParentOfV(v, adj)) {
    				v.childNodes += dfs(adj);
    			}
    		}
    	}
		return v.childNodes;
    }
    
    private boolean isAdjParentOfV(Vertex v, Vertex adj) {
    	if(v.parent != null && v.parent.name == adj.name)
    		return true;
    	return false;
    }
    
    private void collectInput() {
		Scanner scanner = new Scanner(System.in);
		String firstLine = scanner.nextLine();
		
		numberOfVertices = Integer.parseInt(firstLine.split(" ")[0]); 
		numberOfEdges = Integer.parseInt(firstLine.split(" ")[1]);
    	
		for(int i=1; i<=numberOfEdges; i++) {
    		String edge = scanner.nextLine();
    		Vertex adjacentVertex = new Vertex(Integer.parseInt(edge.split(" ")[0]));
    		Vertex parentVertex = new Vertex(Integer.parseInt(edge.split(" ")[1]));
    		
    		if(findVertexInATree(parentVertex) == null) {
    			tree.add(parentVertex);
    		} else {
    			parentVertex = findVertexInATree(parentVertex);
    		}
    		
    		if(findVertexInATree(adjacentVertex) == null) {
    			tree.add(adjacentVertex);
    		} else {
    			adjacentVertex = findVertexInATree(adjacentVertex);
    		}
			
    		parentVertex.addAdjacentVertex(adjacentVertex);
    		adjacentVertex.parent = parentVertex;
    		adjacentVertex.addAdjacentVertex(parentVertex);
    	}
		
		scanner.close();
	}
    
    private Vertex findVertexInATree(Vertex vertex) {
    	for(Vertex v: tree) {
    		if(vertex.name == v.name)
    			return v;
    	}
    	
    	return null;
    }
    
    class Vertex {
    	private int name;
    	private List<Vertex> adjacencyList;
    	Vertex parent = null;
    	private boolean visited = false;
    	private int childNodes = 1;
    	
    	public List<Vertex> getAdjacencyList() {
			return Collections.unmodifiableList(adjacencyList);
		}

		public Vertex(int name) {
			this.name = name;
			adjacencyList = new ArrayList<Vertex>();
		}
    	
    	void addAdjacentVertex(Vertex vertex) {
    		adjacencyList.add(vertex);
    	}
    	
    }
}