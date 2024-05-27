def pascal_triangle(n):
    """Generate Pascal's triangle of size n."""
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        # Start each row with [1]
        row = [1]
        if i > 0:
            # Add the intermediate values
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            # End each row with [1]
            row.append(1)
        
        triangle.append(row)
    
    return triangle
