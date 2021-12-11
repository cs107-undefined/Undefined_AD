Broader Impact and Future Directions
========================================


Broader Impact and Inclusively Statement
------------------------------------------


Future Directions
---------------------

This project is part of the Harvard CS107/AS207: Systems Development for Computational Science class in Fall 2021. 

We have achieved the forward and reverse mode to calculate the derivatives automatically. 
However, there are a few things that we thought about but did not implemented given the limited time. 

Beyond the first order derivative
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Our package can only do the first order derivative. In some cases, you will need to calculate the second order derivative. 
As we briefly mentioned in class, using the Hessian approach could be doable for a second order derivative.
Moreover, if we could let the users to decide how many times they want to take the derivatives (more than 1), that would be highly useful. 

Graphic User Interface (GUI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The consumers and developers can only utilize our package via the command-line interact.
We could develop our package into a GUI interface so that it could be useful for consumers who do not know much about programming. 
One real world example could be in high school class, the teachers could use the computational graph functionality to explain how the derivatives could be calculated in a more precise way than taking the limit. 

Integrated with ML models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since our design and implementation can compute the derivative relatively fast (all the test cases can be finished in 0.05s), we could integrate it with a gradient descent machine learning model to see if it would improve the performance and accuracy. 
This would be highly accepted by the researchers, who have to deal with large amount of data, such as the Electrical Health Records (EHR) and fluid mechanics data. 
Moreover, if this would be possible, we could make a broader impact by integrating the method to cloud ML platforms, such as Azure from Microsoft, so that our package can reach to more consumers and help with their needs.