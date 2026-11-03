# Vertical Slice 15-Minute Playable Prototype (`vertical-slice.md`)
# Sub-Agent Domain: @engine-developer (Godot 4, Unity)
# Integrations: watabou (procedural layout), modly (modular data binding)

## 1. Vertical Slice Objective & Scope
The goal of the 15-minute vertical slice is to validate gameplay feel, art direction, performance, and narrative tone without building an entire game.

### Core Deliverables:
1. **Playable Character:** Smooth 3D movement (WASD + mouse look), dodge/sprint, primary action/attack, camera occlusion collision.
2. **One Complete Encounter Zone:** 1 combat encounter + 1 environmental puzzle/gate + 1 NPC interaction.
3. **Audio-Visual Polish:** PBR stylized lighting, footsteps SFX, ambient sound loop, responsive HUD.
4. **Deterministic End State:** A victory or exit screen concluding the 15-minute experience.

---

## 2. Godot 4.x Character Controller Standard (GDScript)

```gdscript
extends CharacterBody3D
class_name PlayerController

@export var move_speed: float = 6.0
@export var sprint_speed: float = 9.5
@export var acceleration: float = 12.0
@export var jump_impulse: float = 4.5
@export var mouse_sensitivity: float = 0.002

@onready var camera_mount: Node3D = $CameraMount
var gravity: float = ProjectSettings.get_setting("physics/3d/default_gravity")

func _unhandled_input(event: InputEvent) -> void:
    if event is InputEventMouseMotion and Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
        rotate_y(-event.relative.x * mouse_sensitivity)
        camera_mount.rotate_x(-event.relative.y * mouse_sensitivity)
        camera_mount.rotation.x = clamp(camera_mount.rotation.x, deg_to_rad(-70.0), deg_to_rad(60.0))

func _physics_process(delta: float) -> void:
    if not is_on_floor():
        velocity.y -= gravity * delta

    if Input.is_action_just_pressed("jump") and is_on_floor():
        velocity.y = jump_impulse

    var input_dir: Vector2 = Input.get_vector("move_left", "move_right", "move_forward", "move_back")
    var direction: Vector3 = (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
    var target_speed: float = sprint_speed if Input.is_action_pressed("sprint") else move_speed

    if direction != Vector3.ZERO:
        velocity.x = lerp(velocity.x, direction.x * target_speed, acceleration * delta)
        velocity.z = lerp(velocity.z, direction.z * target_speed, acceleration * delta)
    else:
        velocity.x = move_toward(velocity.x, 0, acceleration * delta)
        velocity.z = move_toward(velocity.z, 0, acceleration * delta)

    move_and_slide()
```

---

## 3. Production Milestones (15-Minute Slice)
- **M0 (Day 1):** Greybox blockout in Godot with player controller and camera.
- **M1 (Day 2):** Modular assets imported from Blender (`@3d-artist`).
- **M2 (Day 3):** Combat mechanics, enemy state machine, hit detection wired.
- **M3 (Day 4):** Dialogue trigger box, subtitle UI, audio playback.
- **M4 (Day 5):** QA audit, performance profiling (stable 60 FPS on baseline target).
