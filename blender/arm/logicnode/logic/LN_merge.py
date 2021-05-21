from arm.logicnode.arm_nodes import *


class MergeNode(ArmLogicTreeNode):
    """Activates the output when at least one connected input is activated.
    If multiple inputs are active, the behaviour is specified by the
    `Execution Mode` option.

    @output Active Input Index: [*Available if Execution Mode is set to
        Once Per Input*] The index of the last input that activated the output,
        -1 if there was no execution yet on the current frame.

    @option Execution Mode: The node's behaviour if multiple inputs are
        active on the same frame.

        - `Once Per Input`: If multiple inputs are active on one frame, activate
            the output for each active input individually (simple forwarding).

        - `Once Per Frame`: If multiple inputs are active on one frame,
            trigger the output only once.

    @option New: Add a new input socket.
    @option X Button: Remove the lowermost input socket."""
    bl_idname = 'LNMergeNode'
    bl_label = 'Merge'
    arm_section = 'flow'
    arm_version = 1

    def update_exec_mode(self, context):
        self.outputs['Active Input Index'].hide = self.property0 == 'once_per_frame'

    property0: EnumProperty(
        name='Execution Mode',
        description='The node\'s behaviour if multiple inputs are active on the same frame',
        items=[('once_per_input', 'Once Per Input',
                'If multiple inputs are active on one frame, activate the'
                ' output for each active input individually (simple forwarding)'),
               ('once_per_frame', 'Once Per Frame',
                'If multiple inputs are active on one frame, trigger the output only once')],
        default='once_per_input',
        update=update_exec_mode,
    )

    def __init__(self):
        super(MergeNode, self).__init__()
        array_nodes[str(id(self))] = self

    def init(self, context):
        super(MergeNode, self).init(context)
        self.add_output('ArmNodeSocketAction', 'Out')
        self.add_output('NodeSocketInt', 'Active Input Index')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0', text='')

        row = layout.row(align=True)
        op = row.operator('arm.node_add_input', text='New', icon='PLUS', emboss=True)
        op.node_index = str(id(self))
        op.socket_type = 'ArmNodeSocketAction'
        op2 = row.operator('arm.node_remove_input', text='', icon='X', emboss=True)
        op2.node_index = str(id(self))

    def draw_label(self) -> str:
        if len(self.inputs) == 0:
            return self.bl_label

        return f'{self.bl_label}: [{len(self.inputs)}]'
