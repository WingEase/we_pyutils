import unittest
from pathlib import Path

from we_pyutils.parsers.ieee_ra import oui_txt_parser, OuiRegistry, oui_list_compare


class IeeeRaTestCase(unittest.TestCase):
    data_dir: Path = Path(__file__).parent / 'data'
    ieee_dir: Path = data_dir / 'standards-oui.ieee.org'
    sl = list(ieee_dir.iterdir())
    files = [
        (OuiRegistry.MA_L, 'oui.txt'),
        (OuiRegistry.MA_M, 'mam.txt'),
        (OuiRegistry.MA_S, 'oui36.txt'),
        (OuiRegistry.IAB, 'iab.txt'),
        (OuiRegistry.CID, 'cid.txt'),
    ]

    def test_oui_txt_parser(self):
        rows = oui_txt_parser('')
        self.assertEqual([], rows)

        self.sl.sort(reverse=True)
        last_dir: Path = self.sl[0]
        older_dir: Path = self.sl[1]
        rows = []
        for registry, file_name in self.files:
            oui_path = last_dir / file_name
            with oui_path.open(mode='r', encoding='utf-8') as f:
                content = f.read()
            rows.extend(oui_txt_parser(content, registry=registry))
            pass
        self.assertGreater(len(rows), 45000)  # 几个文件的总数，大于45000，非精确，以后会变化。

    def test_oui_compare(self):
        self.sl.sort(reverse=True)
        dir_count = len(self.sl)
        if (dir_count := len(self.sl)) >= 2:
            last_dir: Path = self.sl[0]
            older_dir: Path = self.sl[1]
            latest_list = []
            older_list = []
            resp = oui_list_compare(latest_list, older_list)

        pass


if __name__ == '__main__':
    unittest.main()
