class Node {
    constructor( data = null ) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor( data = null ) {
        this.head = new Node(data);
    }

    append ( data ) {

        let node = new Node(data);
        let current = this.head;
        while (current.next) {
            current = current.next;
        }
        current.next = node;
        return this.display();
    }

    appendAtHead ( data ) {

        let node = new Node(data);
        node.next = this.head;
        this.head = node;
    }

    appendAt ( data, position ) {

        let node = new Node(data);
        let current = this.head;
        let counter = 1;

        if (position == 1) {
            node.next = this.head
            this.head = node
            return;
        }

        while (current && counter < (position - 1)) {
            current = current.next
            counter++;
        }
        node.next = current.next;
        current.next = node;
    }

    display () {
        let current = this.head;
        let elements = [];
        while (current) {
            elements.push(current.data);
            current = current.next;
        }
        return elements.join("->");
    }
}

let list = new LinkedList(5)
list.append(10)
list.append(2)
list.appendAtHead(9)
list.appendAt(6, 6)
console.log(list.display())
