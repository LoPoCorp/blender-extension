import bpy
from bpy.app.handlers import persistent


# --- Add props if don't exists ---
def ensure_props(obj):
    if obj.type == "EMPTY":
        if "picking_event" not in obj:
            obj["picking_event"] = ""

        if "visibility_sim_var" not in obj:
            obj["visibility_sim_var"] = ""

        if "sound_spawner" not in obj:
            obj["sound_spawner"] = ""

        if "door" not in obj:
            obj["door"] = -1

    if obj.type == "LIGHT":
        light = obj.data

        if "intensity_factor_sim_var" not in light:
            light["intensity_factor_sim_var"] = ""

        if "visibility_sim_var" not in light:
            light["visibility_sim_var"] = ""

    if obj.type == "MESH":
        if "cast_shadows" not in obj:
            obj["cast_shadows"] = True

        if "receive_shadows" not in obj:
            obj["receive_shadows"] = True

        if "emissive_factor_sim_var" not in obj:
            obj["emissive_factor_sim_var"] = ""

        if "picking_event" not in obj:
            obj["picking_event"] = ""

        if "visibility_sim_var" not in obj:
            obj["visibility_sim_var"] = ""

        for mat in obj.data.materials:
            if mat is not None:
                if "replace_with" not in mat:
                    mat["replace_with"] = ""

    if obj.animation_data and obj.animation_data.action:
        action = obj.animation_data.action

        if "progress_sim_var" not in action:
            action["progress_sim_var"] = ""


# --- Update props on selection change ---
@persistent
def selection_handler(scene):
    obj = bpy.context.object
    if obj:
        ensure_props(obj)


def register():
    # Prevent duplicate handlers
    if selection_handler not in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.append(selection_handler)


def unregister():
    if selection_handler in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(selection_handler)


if __name__ == "__main__":
    register()
