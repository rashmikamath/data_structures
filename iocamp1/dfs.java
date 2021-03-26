public static boolean dfs(Graph graph, int target) {    
	for(Node node : graph.getNodes()) {        
		if (node.getState() == State.UNVISITED && dfsVisit(node, target))            
			return true;    }    
		return false;}

public static boolean dfsVisit(Node node, int target) {    
	node.setState(State.VISITING);    
	if (node.getData() == target)        
		return true;    
	for (Node neighbor: node.getNeighbors()) {
		if (neighbor.getState() == State.UNVISITED && dfsVisit(neighbor,target))            
			return true;    }    
		node.setState(State.VISITED);    
		return false;}

/* * Helper Code. Ask interviewer before implementing. */
public enum State {    UNVISITED,    VISITING,    VISITED;}
public class Graph {    List<Node> nodes;    public Graph(List<Node> nodes) {        super();        this.nodes = nodes;    }    public void addNode(Node node) {        nodes.add(node);    }    public List<Node> getNodes() {        return nodes;    }}public class Node {    List<Node> neighbors;    int data;    State state;    public Node(int data) {        super();        this.data = data;        state = State.UNVISITED;        neighbors = new ArrayList<Node>();    }public int getData() {        return data;    }    public void setData(int data) {        this.data = data;    }    public void setState(State state) {        this.state = state;    }    public State getState() {        return state;    }    public void addNeighbor(Node node) {        neighbors.add(node);    }    public List<Node> getNeighbors() {        return neighbors;    }}