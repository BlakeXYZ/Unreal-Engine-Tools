import unreal



def spawn_cube(my_rot_values=None):
    

        location = unreal.Vector()
        rotation = unreal.Rotator(*my_rot_values) # use '*' Operator to unpack my_rot_values tuple and pass elements in as arguments

        # Get the System to Control the Actors
        editor_actor_subs = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

        # We want to create a StaticMeshActor
        actor_class = unreal.StaticMeshActor

        # Place it in the level
        static_mesh_actor =  editor_actor_subs.spawn_actor_from_class(actor_class, location, rotation)

        # Load and add cube to it
        static_mesh = unreal.EditorAssetLibrary.load_asset("/Engine/BasicShapes/Cube")
        static_mesh_actor.static_mesh_component.set_static_mesh(static_mesh)


def print_all_level_actors():
        
        for actor in unreal.EditorActorSubsystem().get_all_level_actors():
                print(actor.get_actor_label())
                        


        