```python
  _____                     __________                             __________                     .__               
_/ ____\______   ____   ____\______   \_______  _______  ______.__.\______   \_______  _______  __|__| ____   ______
\   __\\_  __ \_/ __ \_/ __ \|     ___/\_  __ \/  _ \  \/  <   |  | |     ___/\_  __ \/  _ \  \/  /  |/ __ \ /  ___/
 |  |   |  | \/\  ___/\  ___/|    |     |  | \(  <_> >    < \___  | |    |     |  | \(  <_> >    <|  \  ___/ \___ \ 
 |__|   |__|    \___  >\___  >____|     |__|   \____/__/\_ \/ ____| |____|     |__|   \____/__/\_ \__|\___  >____  >
                    \/     \/                             \/\/                                   \/       \/     \/ 
```


# freeProxyProxies

`freeProxyProxies` is a Python package for fetching proxy lists from various sources.

## Installation

Install `freeProxyProxies` using pip:

```bash
pip install freeProxyProxies
```

## Usage Example

```python
from freeProxyProxies import Proxies

# Create a Proxies instance
proxies = Proxies()

# Get SSL proxy list
ssl_proxies = proxies.ssl_Proxy()

# Get free proxy list
free_proxies = proxies.free_Proxy()

# Get US proxy list
us_proxies = proxies.US_Proxy()

# Get UK proxy list
uk_proxies = proxies.UK_Proxy()

# Get anonymous proxy list
anonymous_proxies = proxies.anonymous_Proxy()

# Get all available proxy lists
all_proxies = proxies.all_Proxy()

# Example of printing proxy lists
print("SSL Proxy List:", ssl_proxies)
print("Free Proxy List:", free_proxies)
print("US Proxy List:", us_proxies)
print("UK Proxy List:", uk_proxies)
print("Anonymous Proxy List:", anonymous_proxies)
print("All Available Proxy Lists:", all_proxies)
```

```python
import freeProxyProxies

# Example of printing proxy lists
print("SSL Proxy List:", ssl_Proxy())
print("Free Proxy List:", free_Proxy())
print("US Proxy List:", US_Proxy())
print("UK Proxy List:", UK_Proxy())
print("Anonymous Proxy List:", anonymous_Proxy())
print("All Available Proxy Lists:", all_Proxy())
```

## Contributions

If you find any issues or would like to contribute code, please visit the GitHub repository [freeProxy](https://github.com/yourusername/freeProxy).

## Author

- Author: Coward
- Email: CryingCoward@proton.me

## License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

- [x] https://www.sslproxies.org/
