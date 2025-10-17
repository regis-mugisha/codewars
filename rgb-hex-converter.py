def rgb(r, g, b):
    # Clamp values between 0 and 255
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    # Convert each to hexadecimal (2 digits, uppercase)
    r_hex_val = f"{r:02X}"
    g_hex_val = f"{g:02X}"
    b_hex_val = f"{b:02X}"

    # Combine and return
    return r_hex_val + g_hex_val + b_hex_val
