#Q17-print the following
"""
     *
    * *
   * * *
  * * * *
 * * * * *
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     * """
for i in range(1,6):
    spaces=5-i
    stars=i*" *"
    print(" "* spaces+stars)
for i in range(4,0,-1):
    spaces=5-i
    stars=i*" *"
    print(" "* spaces+stars)

