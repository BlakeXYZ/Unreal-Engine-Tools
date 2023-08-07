import unreal
from typing import List  # Import the List type from the typing module


	# get all static mesh actors
	# get all materials             of static mesh actors
	# get all textures              of materials
	 
	# get relevant texture data
	# Data maps linear
	# Power of 2 
	# Multiples of 4 or uncompressable
	# Alpha channels do not compress
	# Confirm streaming status

# get all static mesh actors
# Using Class: EditorActorSubsystem
def __get_all_static_mesh_actors():
    
	editor_actor_subsys = unreal.EditorActorSubsystem()
	all_level_actors = editor_actor_subsys.get_all_level_actors()

	staticMeshActors = []
		
	for actor in all_level_actors:
		if isinstance(actor, unreal.StaticMeshActor):
			# print(actor)

			if actor.get_actor_label() == 'Chocolate_Donut2':
				print(f'Getting Single Actor: {actor.get_actor_label()}....') # Print Outliner Name
				staticMeshActors.append(actor)


	return staticMeshActors


# get all materials of static mesh actors
def __get_all_materials_of_sm_actors() -> List[unreal.MaterialInstance]: # Return List with Typehinting

	staticMeshActors = __get_all_static_mesh_actors()
	staticMeshMaterials = []

	for actor in staticMeshActors:
		if isinstance(actor, unreal.StaticMeshActor):		# Type Hinting to get Property of static_mesh_actors
															# static mesh component
															# static mesh compenent inherits from MeshComponent which contains get_material()
			
			materials = actor.static_mesh_component.get_materials()

			for material in materials:
				if isinstance(material, unreal.MaterialInterface): 	# Type hinting to get info about Material
					material_name = material.get_fname()
					material_type = type(material)
					# print('_______________________')
					# print(f'CHECKING MATERIAL "{material_name}" with TYPE "{material_type}"')
					# print('.........')

					if material in staticMeshMaterials: 					# Do not append duplicate materials
						# print(f'{material_name} is already APPENDED, ensure no duplicates... continue')
						continue

					if not isinstance(material, unreal.MaterialInstance): 	# do not append anything that is not MaterialInstance
						# print(f'{material_name} is not isinstance of MaterialInstance... continue')
						continue

					# Only append Material Instances
					# print(f'Appending {material_name}')
					staticMeshMaterials.append(material)
					
	# print('_______________________')
	return staticMeshMaterials


# get all textures of materials
def __get_all_textures_of_materials() -> List[unreal.Texture2D]: # Return List with Typehinting

	staticMeshMaterials = __get_all_materials_of_sm_actors()
	my_textures = []

	for material in staticMeshMaterials:

		# print(type(material)) # = <class 'MaterialInstanceConstant'>
		#							and Base Class = unreal.MaterialInstance
		#							which contains: property texture_parameter_value Type Array(TextureParameterValue)

		tex_parameter_values = material.texture_parameter_values
		for tex_parameter_value in tex_parameter_values: # for each parameter value
			texture = tex_parameter_value.parameter_value # select texture asset of material
			if texture in my_textures: # DO NOT append duplicate textures
				continue
			
			my_textures.append(texture) # append textures to list: staticMeshTextures

	return my_textures

texture_config = {

	'texture_suffix_list': ['D', 'N', 'DpR'],

	'config_per_texture_type': [

		{'type': 'Diffuse',
   					'suffix': 					'D',		
   					'compression': 				unreal.TextureCompressionSettings.TC_DEFAULT,
					'texture_space_sRGB': 		True},

		{'type': 'Normal',
					'suffix': 					'N',		
   					'compression': 				unreal.TextureCompressionSettings.TC_NORMALMAP,
					'texture_space_sRGB':		False},  

		{'type': 'Masks',
					'suffix': 					'DpR',		
   					'compression': 				unreal.TextureCompressionSettings.TC_MASKS,
					'texture_space_sRGB':		False},            
	],
}



def __audit_textures():

	my_textures = __get_all_textures_of_materials()

	unreal.log('-')

	for my_texture in my_textures:
		texture_name = my_texture.get_name()
		texture_resolution = (f'{(my_texture.blueprint_get_size_x())}x{(my_texture.blueprint_get_size_y())}')

		print('---------------------------------')
		print(f'{texture_name} - {texture_resolution} - {my_texture.compression_settings}')

	# Check if SUFFIX is present. IF SUFFIX false: continue to next loop and print warning log of NO SUFFIX
		has_texture_suffix = any(texture_name.endswith(suffix) for suffix in texture_config['texture_suffix_list']) # any function to determine if any suffix in the texture_suffix_list matches the texture_name
		suffix_list = ', '.join(texture_config['texture_suffix_list']) # readable suffix list for warning log

		if has_texture_suffix == False:
			unreal.log_warning(f'MISSING TEXTURE SUFFIX -- Cannot Continue With Texture Audit for {texture_name}')
			unreal.log_warning(f'TEXTURE SUFFIX LIST: {suffix_list}')
			continue  # Skip the rest of the loop and move to the next iteration

	# Continue with AUDIT on Textures that contain SUFFIX
		for texture_types in texture_config['config_per_texture_type']:
			config_texture_type = 				texture_types['type']
			config_texture_suffix =				texture_types['suffix']
			config_texture_compression =		texture_types['compression']
			config_texture_space_sRGB = 		texture_types['texture_space_sRGB']
  
			if texture_name.endswith(config_texture_suffix):								# using dictionary to select texture type
				print(f'Audit Texture as: "{config_texture_type}" Map')								


				if my_texture.compression_settings != config_texture_compression:					# 		Check Compression Settings
					unreal.log_warning(f'WRONG COMPRESSION SETTINGS')
					unreal.log_warning(f'		-- compression should be {config_texture_compression}')

					## DO SOMETHING
					
				else:
					print(f'		Correct Compression')


				if my_texture.srgb != config_texture_space_sRGB:									# 		Check Texture space. sRGB or Linear?
					unreal.log_warning(f'WRONG TEXTURE SPACE sRGB')
					unreal.log_warning(f'		-- sRGB should be set to "{config_texture_space_sRGB}"')

					## DO SOMETHING 

				else:
					print(f'		Correct Texture Space sRGB')

																									#		Check Texture Streaming

																									# culprit of most of the crashing MRQ renders that I come across. 
																									# People export 8k or 4k out of Substance for every single texture in their project 
																									# and then attempt to load them all into VRAM. The GPU gets overwhelmed and crashed.
				if my_texture.never_stream == False:												
					unreal.log_warning(f'Texture Streaming: On')

					## DO SOMETHING 

				else:
					print(f'		Texture Streaming: Off')



				if my_texture.blueprint_get_size_x() != my_texture.blueprint_get_size_y():			#		Check Texture Resolution: SQUARE (1x1 ratio)
					unreal.log_warning(f'Resolution: {texture_resolution} is not SQUARE')

				if __is_power_of_two(my_texture.blueprint_get_size_x()) == False:					#		Check Texture Resolution: POWER OF TWO using custom function
					unreal.log_warning(f'Resolution: {texture_resolution} is not POWER OF TWO')









		# if texture.srgb == True:
		# 	print(f'		Texture Space: sRGB')
		# else:
		# 	print(f'		Texture Space: Linear')

		# if texture.never_stream == True:
		# 	print(f'		Texture Streaming: Off')
		# else:
		# 	print(f'		Texture Streaming: On')

		# if texture.blueprint_get_size_x() != texture.blueprint_get_size_y():
		# 	unreal.log_warning(f'		Resolution: {texture_resolution} is not SQUARE')

		# if __is_power_of_two(texture.blueprint_get_size_x()) == False:
		# 	unreal.log_warning(f'		Resolution: {texture_resolution} is not POWER OF TWO')





#_____________________________________________
# if BASE COLOR/DIFFUSE:
#
#			Compression Settings: Default
#			Texture Space: sRGB
#_____________________________________________
# if NORMAL MAP:
#
#			Compression Settings: Normalmap
#			Texture Space: Linear
#_____________________________________________
# if ALPHA MASK - Metallic, Spec, Roughness etc.
#
#			Compression Settings: Masks
#			Texture Space: Linear
#_____________________________________________
#TODO: for ALL TEXTURES:
#
# 			Has Alpha Channel ?
#			Texture Streaming: OFF
#			Texture Resolution: SQUARE (1x1 ratio)
#			Texture Resolution: POWER OF TWO
#			Check For HDR images
#_____________________________________________


def __is_power_of_two(num):
    # A number is a power of two if it has exactly one bit set to 1.
    return num & (num - 1) == 0 and num != 0
			

def run():
	print('=======================================================================')
	__audit_textures()

run()
    

