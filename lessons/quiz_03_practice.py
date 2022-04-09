class Course: 
    """Models the idea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, prereq: str) -> bool:
        result: bool = False
        if self.level >= 400:
            for name in self.prerequisites:
                if name == prereq:
                    result = True
        return result


pre: list[str] = ["math, psych"]

a: Course = Course()
a.name = "comp"
a.level = 400
a.prerequisites = pre


