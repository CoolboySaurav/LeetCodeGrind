/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) return null;
        
        Map<Node, Node> nodeMap = new HashMap<>();
        Node cur = head;
        
        // First pass: create all nodes and put them in the map
        while (cur != null) {
            nodeMap.put(cur, new Node(cur.val));
            cur = cur.next;
        }
        
        cur = head;
        
        // Second pass: assign next and random pointers
        while (cur != null) {
            Node copy = nodeMap.get(cur);
            copy.next = nodeMap.get(cur.next);
            copy.random = nodeMap.get(cur.random);
            cur = cur.next;
        }
        
        return nodeMap.get(head); // Return the copied head node
    }
}
