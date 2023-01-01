from ctypes_window_info import get_window_infos
from mousekey import MouseKey

coords_clicker = MouseKey()


def get_absolute_screen_coords_of_element(driver, x, y):
    co = get_browser_window_coords(driver)
    return co["offset_x"] + x, co["offset_y"] + y


def get_browser_window_coords(
    driver,
):
    widget1 = "WidgetWin_1"
    bar = 0
    boundingbox = (0, 0, 0, 0)
    aftercheckpids = [driver.browser_pid]
    allei = []
    for g in get_window_infos():
        if g.pid in aftercheckpids:
            for _ in coords_clicker.get_elements_from_hwnd(g.hwnd)["family"]:
                allei.append(_)
    alle = list(set(allei))
    for _ in alle:
        if "Chrome_RenderWidgetHostHWND" in _.title:
            bar = _.coords_win[2]

    for g in get_window_infos():
        if g.pid in aftercheckpids:
            if "WidgetWin" in g.class_name:
                if sum(g.dim_win) > 0:
                    if widget1 in g.class_name:
                        boundingbox = (
                            g.coords_win[0],
                            g.coords_win[2] + bar,
                            g.coords_win[1],
                            g.coords_win[3],
                        )
    offset_x = boundingbox[0]
    offset_y = boundingbox[1]
    height = boundingbox[3] - boundingbox[1]
    width = boundingbox[2] - boundingbox[0]
    center = offset_x + width // 2, offset_y + height // 2
    vara = {
        "offset_x": offset_x,
        "offset_y": offset_y,
        "height": height,
        "width": width,
        "center": center,
    }
    return vara
