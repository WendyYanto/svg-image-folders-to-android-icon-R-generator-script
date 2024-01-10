import os

ICON_FOLDER = "Icons"

# REQUIRED TO FILL
## example: com/company/package/assets
OUTPUT_PATH = ""
## example: com.company.package.assets
PACKAGE_NAME = ""
### example: com.company.package.R
R_PACKAGE_NAME = f"{PACKAGE_NAME}.R"

ICON_EXTENSION = ".svg"

# Common prefix for all icons to clean up
UNFILTERED_PREFIX = "Size=32_"

icons = os.listdir(ICON_FOLDER)

svg_icons = []

def write(file, string, is_last=False):
    file.write(string)
    if not is_last:
        file.write("\n")
    print(string)

# rename icons
for icon in icons:
    icon_key = icon.removeprefix(UNFILTERED_PREFIX).lower()
    new_icon_name = "donut_ic_" + icon_key
    svg_icons.append((icon_key.removesuffix(ICON_EXTENSION), new_icon_name.removesuffix(ICON_EXTENSION)))

    folder = ICON_FOLDER + "/"
    os.rename(folder + icon, folder + new_icon_name)

# generate enums
if os.path.exists(OUTPUT_PATH):
    print("Delete file: " + OUTPUT_PATH)
    os.remove(OUTPUT_PATH)

donut_enum_file = open(OUTPUT_PATH, "w+")
print("-- Create file: " + OUTPUT_PATH)

write(donut_enum_file, f"package {PACKAGE_NAME}\n")
write(donut_enum_file, "import androidx.annotation.DrawableRes")
write(donut_enum_file, f"import {R_PACKAGE_NAME}\n")

write(donut_enum_file, "enum class DonutSystemIcon(")
write(donut_enum_file, "    @DrawableRes")
write(donut_enum_file, "    val resource: Int")
write(donut_enum_file, ") {")

for icon in svg_icons:
    icon_key = icon[0].upper()
    icon_drawable_name = icon[1]

    icon_enum = f"{icon_key}(R.drawable.{icon_drawable_name}),"
    write(donut_enum_file, f"    {icon_enum}")

write(donut_enum_file, "}")

donut_enum_file.close()