#Q14-print the following pattern
"""		    *
	     *  *
      *  *  *
   *  *  *  *
*  *  *  *  * """

for i in range(1,6):
    spaces=5-i
    stars=i*"*"
    print(" "* spaces+stars)

