extends Area2D

func _physics_process(delta):
	var enemies_in_range = get_overlapping_bodies()
	var e_in = get_overlapping_areas()
	if (enemies_in_range.size() >0 || e_in.size()>0):
		var target_enemy = enemies_in_range.front()
		look_at(target_enemy.global_position)
	if (Input.is_action_just_pressed("attack")):
		isAttackClick()
	

func shoot():
	const BULLET = preload("res://bullet.tscn")
	var new_bullet = BULLET.instantiate()
	new_bullet.global_position = %ShootingPoint.global_position
	new_bullet.global_rotation = %ShootingPoint.global_rotation
	
	%ShootingPoint.add_child(new_bullet)

func isAttackClick():
	shoot()

