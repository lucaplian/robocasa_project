import numpy as np
list_classes = []
#RUN THIS FILE IN THE ROBOCASA FOLDER
#IN ROBOCASA put in the robocasa.demos folder and then run python/mjpython(for MAC users) -m demos.open_program
from robocasa.environments.kitchen.single_stage.kitchen_coffee import (
    CoffeePressButton,
    CoffeeServeMug,
    CoffeeSetupMug,
)
list_classes.extend([CoffeePressButton, CoffeeServeMug, CoffeeSetupMug])
from robocasa.environments.kitchen.single_stage.kitchen_doors import (
    CloseDoor,
    CloseDoubleDoor,
    CloseSingleDoor,
    OpenDoor,
    OpenDoubleDoor,
    OpenSingleDoor,
)
list_classes.extend([CloseDoor, CloseDoubleDoor, CloseSingleDoor, OpenDoor, OpenDoubleDoor, OpenSingleDoor])

from robocasa.environments.kitchen.single_stage.kitchen_drawer import (
    CloseDrawer,
    OpenDrawer,
)

list_classes.extend([CloseDrawer, OpenDrawer])

from robocasa.environments.kitchen.single_stage.kitchen_microwave import (
    TurnOffMicrowave,
    TurnOnMicrowave,
)
list_classes.extend([TurnOffMicrowave, TurnOnMicrowave])

from robocasa.environments.kitchen.single_stage.kitchen_navigate import NavigateKitchen
list_classes.extend([NavigateKitchen])

from robocasa.environments.kitchen.single_stage.kitchen_pnp import (
    PnPCabToCounter,
    PnPCounterToCab,
    PnPCounterToMicrowave,
    PnPCounterToSink,
    PnPMicrowaveToCounter,
    PnPSinkToCounter,
)
list_classes.extend([PnPCabToCounter, PnPCounterToCab, PnPCounterToMicrowave, PnPCounterToSink, PnPMicrowaveToCounter, PnPSinkToCounter])

from robocasa.environments.kitchen.single_stage.kitchen_sink import (
    TurnOffSinkFaucet,
    TurnOnSinkFaucet,
)

list_classes.extend([TurnOffSinkFaucet, TurnOnSinkFaucet])

from robocasa.environments.kitchen.single_stage.kitchen_stove import (
    TurnOffStove,
    TurnOnStove,
)
list_classes.extend([TurnOffStove, TurnOnStove])
# IT TELLS YOU, IF YOU DID YOUR TASK SUCCESFUL OR NOT
def do_task(our_class):

    env = our_class(
        robots="PandaMobile",
        has_renderer=True,
        has_offscreen_renderer=False,
        use_camera_obs=False,
        horizon=500,
    )

    env.reset()
    print(f"Task: {env.get_ep_meta()['lang']}")
    print(f"Action dim: {env.action_dim}")

    success = False
    for step in range(env.horizon):
        action = np.zeros(env.action_dim)

        #COMMANDS FOR HAND, ROBOT AND GRIPPER
        # Significance of the components
        # movements of the end-effector(hand) are represented by actions from 0 to 2
            #0: operates in the z axis, the robot leans back(the hand is in direction +Δz)
            #with positive he leans forward(the hand is in direction -Δz)
            #1: operates in the x axis, hand goes to the right, with negative value, with positive to the left
            #2: operates in the y axis, if it is negative, the end-effector goes down, if positive, it goes up
        # rotations of the end-effector(hand) are represented by actions from 3 to 5
            #3: rotation around z axis
            #4: rotation around x axis
            #5: rotation around y axis
        #(if you rotate it too much, at some point it can no longer
        # just with the wrist and starts to "reorient" the entire robot)
        # the next apply to the whole robot from 6 to 9:
            #6: the "ankles" of the robot are raised if positive, they go down if negative
            #7: translation in the z axis, it moves the whole robot backward if negative, forward if positive
            #8: translation in the x axis, it moves the whole robot to the left, if positive;
            # the whole robot goes to the right, if negative
            #9: rotation of the base in the plane: if positive it rotates counterclockwise to the left,
            # if negative it rotates clockwise
        # This command applies to the gripper
            #10: gripper control: if values is positive, it tries to close the gripper, the negative values, it tries to open the gripper, 
                #in state it keeps the gripper neutral, on 0.0 it is closed
        # This is a mode switch for how the arm goal is updated
            #11: action_mode:
            # if positive, it is in BASE MODE. In this mode, the robot tries to follow a predefined path ("planned/desired" goal)
            # in order to keep the hand on a trajectory. This takes into consideration scenarious 
            # where the robot is moving, for the reason being that it assists in keeping the planned trajectory,
            # thus providing more stable movements. It should be used when the robot is moving.
            # if negative or zero, it is in ARM MODE. In this mode, the robot does not have a predefined path, this is local based movement. 
            # The robot tries to do a movement based on the current state/position. It should be used when the robot stands still.

        if step < 200:
            action[0] = 0.0   
                            
            action[1] = 0.0   
            action[2] = 0.0    
            action[3] = 0.2 
            action[4] = 0.0   
            action[5] = 0.0 
            action[6] = 0.0   
            action[7] = 0.3 
            action[8] = 0.0 
            action[9] = 0.0 
            action[10] = 0.0 
            action[11] = -0.1

        else:
            action[0] = 0.0
            action[1] = 0.0
            action[2] = 0.0
            action[7] = 0.3 
            action[6] = 0.0
            action[3] = 0.2
            action[11] = 0.1



        obs, reward, done, info = env.step(action)
        env.render()

        if env._check_success():
            print(f"Task successful at step {step}")
            success = True
            break

    if not success:
        print("Task NOT successful")

    env.close()

if __name__ == "__main__":
    print("Here is a list of {}s:\n".format(list_classes))

    s = input(
            "Choose an classes option from 0 to {}, or any other key for default ({}): ".format(
                len(list_classes) - 1,
                list_classes[0],
            )
        )
        # parse input into a number within range
    k = min(max(int(s), 0), len(list_classes) - 1)
    do_task(list_classes[k])