# Changelog

All notable changes to the **AI-Powered Analysis in Smart Home Environment** project will be documented here.


## [0.1.0] – 2025-10-11
### Added
- Created project repository structure (`/src`, `/data`, `/notebooks`, `/docs`).
- Added initial README.md with project goals and domain description.

## [0.1.1] – 2025-10-11
### Added
- added datasets references
- HA using IoT.docx, explaining my project


## [0.2.0] – 2025-10-26
### Modified the theme of the diploma project
- Centred around robocasa framework now
- Created markdown documents in docs such as dataset_notes.md, kitchen_map.md. The document dataset_notes.md explains the hdf5 format, and explain the findings inside a demo; kitchen_map.md explains the layout of a kitchen
- Added data
- the yaml gives the conceptual scheme, but with rules, preconditions  and plan, where we iterate our atomic actions

## [0.2.1] – 2025-10-28
### Added BT tree for simple and complex
- added BT_complex.mmd and BT_simple.mmd, which the simple one explains the order of atomic actions, while the complex one puts the diagrams which try to emulate iteration of an atomic actions.


## [0.2.2] – 2025-11-11
### coloured BT and made the diploma project with LLM
- coloured the atomic tasks for BT_complex.mmd
- made the diploma project with LLM (it is to be rewritten again based on my own writing, research papers etc., just serves as a base)


## [0.2.2.1] – 2025-11-13
### REMOVED OBSOLETE DOCUMENTS
- removed dataset_references.txt
- added initialization flow for robosuite, helping in understanding how robosuite works


## [0.2.2.2] – 2025-11-14
### REFORMATING FOLDERS AND ADDED EXPLAINATION for demo_teleop
- reformat folders, included new folder such as docs for word documents such as "ROBOCASA PROJECT 2.0 1.docx" and "robosuite_initialization_flow.docx"
- added "robosuite_initialization_flow_teleop.docx" - explains demo_teleop from robocasa, which will serve as the basis for our implementation.

## [0.2.3] – 2025-11-27
### Added demo code which opens the atomic tasks environment
 - added open_program.py, which is a program, where it contains all the atomic tasks environment, which can be called by inputting a number from 0 to 23. Inside there is an explained action array, which contains 12 values, and all of them are explained in the order for the user to understand what each value means. Additionally, the evironment is rendered for better understanding of the tasks.
 - added docs/Detailed Technical Explanation- Control Flow and Action Semantics.docx, which explains throughly the control flow of the environments in general and what each action means in detail.


