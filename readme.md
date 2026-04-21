# 🏗️ Unitree go1 Dog

**Aurora Robotics** - **Sayande Project**

- **Lead Contributor:** [Agwaze Great Osayande](https://github.com/GreatOsa), [Saheeed Olanrewaju Sulaiman](https://github.com/Saheed-Olanrewaju-Sulaiman)

A ROS-integrated Gazebo simulation of the Unitree Go1 quadruped for development, debugging, and validation of robotic behaviors.

---

## 📌 Project Vision

This project exists to provide a safe, reproducible, and simulation-first environment for studying and developing behaviors for the Unitree Go1 quadruped robot.

The long term goal is to build a robust quadruped robotics stack—covering locomotion, sensing, navigation, and autonomy using the Unitree Go1 as a reference platform. This simulation serves as the foundation for validating kinematics, dynamics, sensor integration, and control strategies under controlled conditions.

---

## 🧱 Scope of This Repository

⚠️ Read this first. This repository focuses strictly on simulation and experimentation, not physical robot deployment.

**This repository includes:**

- A simulation model of the Unitree Go1 quadruped (URDF/SDF, links, joints, and frames)

- Physics-based simulation setup (Gazebo / ROS integration)

<!-- - Basic sensor definitions (e.g. IMU, camera, or LiDAR if present) -->

- Launch files and configuration for running the robot in simulation

**This repository does NOT include:**

- Firmware or low-level motor drivers

- Real hardware calibration or actuator tuning

- Safety-certified control software for physical deployment

- Production-ready autonomy or perception systems

One sentence summary:

> This repository defines how the Unitree Go1 behaves in simulation, not how it operates on real hardware.

---

## 🏗️ What Is Modeled / Implemented

At its current stage, this project focuses solely on establishing a Gazebo-based simulation environment.

✔ Current Implementation

- A URDF model defining the Unitree Go1’s links, joints, and kinematic structure

- A Gazebo world setup for running and visualizing simulations and RViz setup

<!-- - Basic world elements such as ground plane, lighting, and physics configuration -->

- Launch and configuration files required to spawn the robot in Gazebo

🚧 Not Yet Implemented

- High-fidelity actuator dynamics and motor controllers

- Sensor plugins beyond basic definitions (e.g. vision, LiDAR, advanced IMU)

- ROS control interfaces and gait controllers

- Navigation, perception, or autonomy systems

### ✔ Core Components

- Unitree Go1 URDF model defining links, joints, and coordinate frames

- Gazebo simulation world for spawning and visualizing the robot

- Physics configuration for basic interaction with the environment

- Launch and configuration files for initializing the simulation

<!-- ### Design Constraints & Assumptions

-
- *** -->

## 📂 Repository Overview

This project is intended as a simulation foundation, not a complete robotics system, and will be extended over time with controllers, sensors, and higher-level autonomy modules.

---

## 🛠️ Tools & Technologies

- **Primary Software: Gazebo Classic 11, ROS (Humble)**

- **Languages / Formats: URDF (XML), Bash**

- **Frameworks / Simulators: Gazebo simulation environment, ROS launch system**

- **Version Control / Tooling: Git, GitHub, and URDF assets**

---

<!-- ## 📁 Project Structure

Explain how the repo is organized.

```
project-root/
│
├── src/              # Core source files
├── assets/           # Models, meshes, media
├── config/           # Configuration files
├── docs/             # Documentation
├── scripts/          # Utility or setup scripts
├── README.md
└── .gitignore
```

Add short comments only where necessary. -->

---

## ▶️ How to Use / Run

### Prerequisites

- Ubuntu 20.04 or 22.04
- Gazebo Classic 11 installed
- ROS Humble (with ros_control and gazebo_ros packages)
- Python 3 (for launch and helper scripts)

### Basic Usage

```bash
git clone https://github.com/GreatOsa/unitree-go-1-dog.git
```

```bash
cd unitree-go-1-dog
colcon list
colcon build
source install/setup.bash
```

```bash
# to open the robot in gazebo

ros2 launch unitreedog_description display.launch.py

```

### Expected Output

- When the simulation is launched successfully:
- Gazebo opens with the Unitree Go1 robot spawned in the world
- The robot appears lying on the ground in its default pose
- The scene includes lighting, a flat ground plane, and basic physics
- The robot is static (no controllers yet), but its links and joints are correctly visualized

> Future updates will enable motion, controllers, and sensors, but currently the output is a stable, well-structured robot ready for further development.

---

<!--


## 👁️ Visual References (Optional)

Brief description of screenshots, diagrams, or renders.

- Stored in: `/images` or `/docs/media`
- Purpose of visuals (layout, geometry, debugging, etc.)

---



## 🚀 Roadmap

What comes next.

- [ ] Next planned feature or phase
- [ ] Integration target (simulation, hardware, perception, etc.)
- [ ] Known limitations

---


## 🧭 Project Status

- **Stage:** Concept / Active Development / Stable / Archived
- **Intended Audience:** Internal / Research / Open Source
- **Maintainers:**

---

-->
<!--

## 🧠 Summary

One or two sentences that answer:

> What problem does this project solve, and why should anyone care?

---



## 📄 License (Optional)

State license or usage restrictions.

---

## 🤝 Contributing (Optional)

Brief rules or expectations for contributors.

---

-->
