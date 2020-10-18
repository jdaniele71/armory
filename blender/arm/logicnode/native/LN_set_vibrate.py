from arm.logicnode.arm_nodes import *
import arm.utils

class SetVibrateNode(ArmLogicTreeNode):
    """Pulses the vibration hardware on the device for time in milliseconds, if such hardware exists."""
    bl_idname = 'LNSetVibrateNode'
    bl_label = 'Set Vibrate'
    arm_version = 1

    def init(self, context):
        super(SetVibrateNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketInt', 'Milliseconds')
        self.inputs[-1].default_value = 100
        self.add_output('ArmNodeSocketAction', 'Out')
        # Add permission for target android
        arm.utils.add_permission_target_android(arm.utils.PermissionName.VIBRATE)

add_node(SetVibrateNode, category=PKG_AS_CATEGORY, section='Native')
