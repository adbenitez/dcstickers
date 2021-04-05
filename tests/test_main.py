import os
import sys

import pytest
from dcstickers.main import main


def test_main() -> None:
    # missing required argument
    with pytest.raises(SystemExit):
        main()

    sys.argv.append(
        "https://signal.art/addstickers/#pack_id=02ded3e66c72e0b04f755642b163069b&pack_key=060cd7e3ebeb601e960c0d26dc08ead960a13ff662c978c543ea5289ceaac58c"
    )
    # can't find DeltaChat config folder
    with pytest.raises(ValueError):
        main()

    cfg_dir = os.path.expanduser("~/.config/DeltaChat/")
    os.mkdir(cfg_dir)
    main()
    stickers_dir = os.path.join(cfg_dir, "stickers")
    packs = os.listdir(stickers_dir)
    assert len(packs) == 1
    assert len(os.listdir(os.path.join(stickers_dir, packs[0])))
