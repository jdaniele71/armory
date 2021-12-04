package armory.logicnode;

class GroupInputNode extends LogicNode {

	public function new(tree: LogicTree) {
		super(tree);
	}

	override function run(from: Int) {
		runOutput(from);
	}

	override function get(from: Int): Dynamic {
		return inputs[from].get();
	}
}
