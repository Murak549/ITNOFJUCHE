def generate_hoi4_focus():
    focus_id = input("Enter focus id: ")
    icon = input("Enter icon name: ")
    prerequisite = input("Enter prerequisite focus id (if any): ")
    relative_position_id = input("Enter relative position id (if any): ")
    cost = input("Enter focus cost (if any): ")
    locate_x = input("Enter locate (x): ")
    locate_y = input("Enter locate (y): ")

    focus_code = f"""
focus = {{
    id = {focus_id}
    icon = {icon}
"""

    if prerequisite:
        focus_code += f"    prerequisite = {{ focus = {prerequisite} }}\n"

    focus_code += f"""
    x = {locate_x}\n
    y = {locate_y}\n
    """

    if relative_position_id:
        focus_code += f"    relative_position_id = {relative_position_id}\n"

    if cost:
        focus_code += f"    cost = {cost}\n"

    focus_code += """
    ai_will_do = {
        factor = 1
    }

    available_if_capitulated = yes

    completion_reward = {

    }
}
"""

    return focus_code

print(generate_hoi4_focus())
