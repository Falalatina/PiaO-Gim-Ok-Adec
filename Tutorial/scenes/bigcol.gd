extends Area2D

@onready var game_manager = %GameManager

func _on_body_entered(body):
	if  (body.name == "MC"):
		queue_free()
		game_manager.add_point(1)
