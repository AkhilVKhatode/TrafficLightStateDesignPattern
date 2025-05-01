# Traffic Light State Design Pattern

This project demonstrates the **State Design Pattern** applied to a traffic light system. The system includes different states for the traffic light, such as **Red**, **Green**, **Yellow**, **Blinking**, and **Maintenance**. Each state represents a different condition of the traffic light, and the light automatically transitions between these states in a defined sequence.

## Project Overview

The traffic light system consists of the following components:
- **TrafficLightContext**: This is the context class that holds the current state and delegates the state transitions to the state object.
- **TrafficLightState**: An abstract class (or interface) that defines the common behavior for all concrete states.
- **Concrete States**: These are the different states of the traffic light:
  - **RedState**: The traffic light is red.
  - **GreenState**: The traffic light is green.
  - **YellowState**: The traffic light is yellow.
  - **BlinkingState**: The traffic light is blinking (e.g., during maintenance).
  - **MaintenanceState**: The traffic light is under maintenance.

The traffic light changes states automatically based on predefined transitions, making the system easily extensible for adding new states.

## How It Works

The **TrafficLightContext** starts in the `RedState`. Upon triggering the `next()` method, the traffic light transitions through the states in the following order:
1. **RedState** -> **GreenState**
2. **GreenState** -> **YellowState**
3. **YellowState** -> **RedState**
4. **RedState** -> **GreenState**

Additionally, states like **BlinkingState** and **MaintenanceState** can be added to handle special conditions (e.g., during maintenance mode).

## Features
- Demonstrates the **State Design Pattern**.
- Easy to extend by adding new states (e.g., Blinking, Maintenance).
- Encapsulates state-specific behavior and transitions in their respective state classes.
