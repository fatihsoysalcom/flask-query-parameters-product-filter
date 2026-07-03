# Flask Query Parameters Product Filter

This example demonstrates how a server-side application (using Flask) can process HTTP query parameters to filter and sort data. It simulates a product listing API where users can specify a `category` and `sort_by` criteria in the URL, and the server responds with the appropriately filtered and sorted list of products. This illustrates how query parameters enable dynamic data retrieval based on client requests.

## Language

`python`

## How to Run

1. Save the code as `app.py`.
2. Install Flask: `pip install Flask`.
3. Run the application: `python app.py`.
4. Open your browser or use `curl` to visit `http://127.0.0.1:5000/` for instructions, or directly try URLs like `http://127.0.0.1:5000/products?category=Electronics&sort_by=price_desc`.

## Original Article

This example accompanies the Turkish article: [Web'de Bilgiye Erişimin Temel Taşı: HTTP Sorgu Parametreleri Nedir?](https://fatihsoysal.com/blog/webde-bilgiye-erisimin-temel-tasi-http-sorgu-parametreleri-nedir/).

## License

MIT — see [LICENSE](LICENSE).
