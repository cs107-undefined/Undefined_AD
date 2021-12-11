Broader Impact and Future Directions
========================================


Broader Impact and Inclusively Statement
------------------------------------------

The ability to calculate and reason about change is essential for a vast range of applications and used to investigate and solve technological and societal problems. Thus the ability to evaluate derivatives, the mathematical study of change, efficiently and accurately is imperative. Our tool, ``Undefined``, calculates simple and complex derivatives using automatic differentiation (AD) in the forward mode and the reverse mode. In comparison to traditional methods of evaluating derivatives (e.g. symbolic differentiation) that are costly to compute and lack accuracy/stability, computing derivatives using AD allows calculations to be performed at machine precision and without compromising accuracy and stability. We believe that this tool will be well accepted by students and researchers looking to quickly and accurately calculate change. The broader impact of this tool will be the ability to investigate and provide understanding of or solutions to issues at a faster rate. In addition, the ability to calculate complex derivatives while utilizing less computational energy is beneficial to anyone who does not have access to much energy; overall, utilizing less energy for computing can also have a positive impact on our climate. Another impact and positive implication of this tool is the ability to visually reason about the solution of a simple or complex derivative. Our computational graph allows users to better understand their output. This is useful in many ways from researchers or professionals understanding lab results, financial or voting predictions to students learning about derivatives. 

We believe that our tool is well developed and produces fast and accurate results, but we understand that it is only useful if there are no barriers to accessing the tool or understanding the tool. Therefore, we have ensured that our software is inclusive to the broader community by making it free and publicly available and include clear documentation on how to install and use. As a result of the tool being open source, users and developers can utilize the tool as we intended as well as contribute to the code base if there is a need for them to modify based on their use case. If a community member creates a pull request, the four developers of the tool will meet to review the modifications and collaborate with the initiator if there are questions. We look forward to community members, novice and experienced, utilizing and contributing to our tool as they solve their unique problems or learn about computational mathematics.



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