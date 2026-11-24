def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}....")
        result = func(*args, **kwargs)
        print("Done")
        return result

    return wrapper


@log_call
def sum_to_n(n):
    return sum(range(1, n + 1))


print(sum_to_n(5))


def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)

                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")

                    if attempt == times - 1:
                        raise

        return wrapper

    return decorator


import random


@retry(times=3)
def test_function():
    if random.random() < 0.7:
        raise Exception("Random failure")

    return "Success!"


print(test_function())


import tempfile
import os


class TempFile:

    def __enter__(self):
        self.temp = tempfile.NamedTemporaryFile(
            mode="w+", delete=False, encoding="utf-8"
        )

        self.filepath = self.temp.name
        return self.temp

    def __exit__(self, exc_type, exc_value, traceback):
        self.temp.close()
        os.remove(self.filepath)


with TempFile() as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

    f.seek(0)

    print(f.read())
