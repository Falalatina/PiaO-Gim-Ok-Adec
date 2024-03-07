extends Node
@onready var points_label = %PointsLabel
@onready var p_2 = $"../End/P2"
@onready var l_2 = $"../End/P2/L2"


var points = 0

func add_point(type):
	
	if  (type == 1):
		points += 4
	else:	
		points +=1
	print(type)
	points_label.text = "Points: " + str(points)
	if (points >= 9):
		p_2.visible =true
		l_2.text =  "You won!! You can continue to collect things anyway..."
