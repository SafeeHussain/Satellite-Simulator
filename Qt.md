---
Qt common practices when making code
---

1. Code Structure and Modularity
    - Keep your code organised into functions and classes
    - Larger applications consider using
        - model
        - view
        - controller
    - ^ architecture

2. Memory Management
    - Make sure to properly disconnect signals and slots when objects are no longer needed
    - release any resources that are no longer in use

3. Performance Optimisation
    - Avoid unneccesary redrawing of widgets
    - Optimise any algorithms or data processing that occurs in the application

4. ~~Cross-Platform Consideration~~ 
    - Ensure different platforms are able to work out
    - Different platforms will lead to different behaviours

