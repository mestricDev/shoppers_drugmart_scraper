# Shoppers Drug Mart Pharmacy Scraper

This script scrapes data about pharmacies from Shoppers Drug Mart's website, such as the pharmacist's name, drug store name, street address, city, province, postal code, and phone number. It will save the scraped data into a CSV file (`pharmacies.csv`) and log any missing or inaccessible data to a separate file (`missing_data.txt`).

## Dependencies

- Python 3.x
- Selenium WebDriver
- Google Chrome
- ChromeDriver

## Required Libraries

Make sure you have the following Python libraries installed:

- selenium
- requests
- csv

You can install them using pip:

```bash
pip install selenium requests
```

## Usage

1. **Set Up ChromeDriver**: Make sure you have ChromeDriver installed and specify its path in the script, e.g., `'C:\\Temp\\chromedriver.exe'`.
2. **Set Up Chrome Binary**: Specify the path to your Chrome executable in the script, e.g., `'C:\\Temp\\chrome-win64\\chrome.exe'`.
3. **Adjust Start and End Values**: You can adjust the `start_num` and `end_num` variables in the script to specify the range of pages to scrape.
4. **Run the Script**: Simply run the script by executing the following command:

```bash
python <path_to_script.py>
```

The data will be saved into `pharmacies.csv`, and any missing data will be recorded in `missing_data.txt`.

## Structure of the Output CSV

The `pharmacies.csv` file will contain the following columns:

- First name
- Last name
- Store number
- Drug store name
- Street address
- City Province Postal code
- Phone

## License

This project is licensed under the MIT License - see the LICENSE.md file for details, or you can include the full text of the MIT License directly in the README as follows:

## Disclaimer

This script is provided for educational purposes only. Always ensure that you are complying with the website's Terms of Service when scraping data.

## Contact

For any inquiries, please contact [your-email@example.com].

---

You may need to adjust some parts to fit your specific needs, like contact information or additional features you might add later.
