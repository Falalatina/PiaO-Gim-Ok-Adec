extends CharacterBody2D
@onready var sprite_2d = $Sprite2D


func _physics_process(delta):
	var direction = Input.get_vector("goLeft", "goRight", "goTop", "goDown")
	velocity = direction * 600
	move_and_slide()
	
	if (velocity.length() > 0.0):
		sprite_2d.animation = "run"
	else:
		sprite_2d.animation = "default"
	var isLeft = velocity.x <0
	sprite_2d.flip_h = isLeft
