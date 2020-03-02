c = get_config()

c.CourseDirectory.course_id = "sam"

c.CourseDirectory.release_directory = 'probs'
c.CourseDirectory.source_directory = 'sol'

c.BaseConverter.force = True

c.GenerateAssignment.force = True
c.GenerateAssignment.no_database = True
