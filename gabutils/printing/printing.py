import warnings

# Try to import colorama
try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
except ImportError:

    class ColorFallback():
        __getattr__ = lambda self, name: ''

    Fore = Back = Style = ColorFallback()
    warnings.warn('Install colorama for colorsupport.')


class Printing(object):
    """ Shortcuts to different printer functions

        Named Printing, but only returns formatted text
    """

    def __init__(self, newline=1, color=False):
        self.newline = newline
        if self.newline > 0:
            self.n = newline * '\n'
        else:
            self.n = ''
        self.color = color

    def _newlinecheck(self, newline):
        if newline is None:
            return self.n
        if newline == 0:
            return ''
        if newline > 0:
            n = newline * '\n'
            return n
        if newline < 0:
            warnings.warn("'newline' arg cannot be negative. Using 0.")
            return ''
        else:
            raise Exception('Something failed')

    def h1(self, text, newline=None):
        n = self._newlinecheck(newline)
        result = f"{n}{'=':=^80}\n{text:^80}\n{'=':=^80}"
        return result

    def h2(self, text, newline=None):
        n = self._newlinecheck(newline)
        result = f"{n}{'-':-^80}\n{text:^80}\n{'-':-^80}"
        return result

    def h3(self, text, newline=None):
        n = self._newlinecheck(newline)
        text = f" {text} "
        result = f"{n}{text:^80}\n{'=':=^80}"
        return result

    def h4(self, text, newline=None):
        n = self._newlinecheck(newline)
        text = f" {text} "
        result = f"{n}{text:^80}\n{'-':-^80}"
        return result

    def h5(self, text, newline=None):
        n = self._newlinecheck(newline)
        text = f"  {text}  "
        result = f"{n}{text:=^80}"
        return result

    def h6(self, text, newline=None):
        n = self._newlinecheck(newline)
        text = f"  {text}  "
        result = f"{n}{text:-^80}"
        return result

    def ok(self, text):
        if self.color:
            return (
                Style.BRIGHT + Fore.GREEN + '[+] ' + Style.RESET_ALL + text)
        else:
            return ('[+] ' + text)

    def fail(self, text):
        if self.color:
            return (Style.BRIGHT + Fore.RED + '[-] ' + Style.RESET_ALL + text)
        else:
            return ('[-] ' + text)

    # true/false print
    def bool(self, text, bool):
        if bool:
            return self.ok(text)
        else:
            return self.fail(text)

    # Something is running
    def run(self, text):
        if self.color:
            return (
                Style.BRIGHT + Fore.WHITE + '[~] ' + Style.RESET_ALL + text)
        else:
            return ('[~] ' + text)

    # Information
    def info(self, text):
        if self.color:
            return (
                Style.BRIGHT + Fore.WHITE + '[*] ' + Style.RESET_ALL + text)
        else:
            return (
                Style.BRIGHT + Fore.WHITE + '[*] ' + Style.RESET_ALL + text)

    # Warning
    def warn(self, text):
        if self.color:
            return (
                Style.BRIGHT + Fore.YELLOW + '[!] ' + Style.RESET_ALL + text)
        else:
            return ('[!] ' + text)

    def inpt(self, text):
        if self.color:
            return (
                Style.BRIGHT + Fore.MAGENTA + '[?] ' + Style.RESET_ALL + text)
        else:
            return ('[?] ' + text)

    # [#] [?] []


if __name__ == '__main__':
    prt = Printing()
    print(prt.h1("Class newline (1)"))
    print(prt.h1("Newline 0", newline=0))
    print(prt.h1("Newline 4", newline=4))
    print(prt.h1("Newline -4", newline=-4))

    pr = Printing(newline=2)
    print(pr.h1('Header 1'))
    print(pr.h2('Header 2'))
    print(pr.h3('Header 3'))
    print(pr.h4('Header 4'))
    print(pr.h5('Header 5'))
    print(pr.h6('Header 6'))

    print(pr.bool('Sykt bra', True))
    print(pr.bool('Mega fail', False))
    print(pr.info('Informatica'))
    print(pr.warn('Shit be careful!'))
    print(pr.run('Scanning for file'))
