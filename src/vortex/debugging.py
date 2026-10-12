def debug(name, frame):
    return f"[DEBUGGING_FTSERV_REF] {name}.{frame.f_code.co_name}:{frame.f_lineno}"
