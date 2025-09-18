<!DOCTYPE html>
<html>
<head>
    <title>Movie Finder</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="bg-dark text-light">
<div class="container mt-4">
    <h1 class="text-center">🎬 Movie Finder</h1>

    <!-- Search Form -->
    <form method="POST" class="d-flex justify-content-center mb-4">
        <input type="text" name="movie" class="form-control w-50" placeholder="Enter movie name...">
        <button class="btn btn-primary ms-2">Search</button>
    </form>

    <!-- Movie Details -->
    {% if movie %}
        <div class="card mb-4 p-3 bg-secondary">
            <h2>{{ movie.Title }} ({{ movie.Year }})</h2>
            <p><strong>Genre:</strong> {{ movie.Genre }}</p>
            <p><strong>Plot:</strong> {{ movie.Plot }}</p>
            <img src="{{ movie.Poster }}" alt="Poster" style="max-height:300px;">
        </div>
    {% endif %}

    <!-- Related Movies -->
    {% if related_movies %}
        <h3>🔗 Related Movies:</h3>
        <div class="row">
            {% for rm in related_movies %}
                <div class="col-md-3 mb-3">
                    <div class="card p-2">
                        <h5>{{ rm.Title }}</h5>
                        <img src="{{ rm.Poster }}" style="max-height:200px;">
                    </div>
                </div>
            {% endfor %}
        </div>
    {% endif %}

    <!-- Default Movies -->
    {% if default_movies %}
        <h3>🔥 Popular Movies:</h3>
        <div class="row">
            {% for dm in default_movies %}
                <div class="col-md-3 mb-3">
                    <div class="card p-2">
                        <h5>{{ dm.Title }}</h5>
                        <img src="{{ dm.Poster }}" style="max-height:200px;">
                    </div>
                </div>
            {% endfor %}
        </div>
    {% endif %}
</div>
</body>
</html>
