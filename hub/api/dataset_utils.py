from typing import Union
from hub.codec import PngCodec, Lz4, NumPy, Zstd, JpegCodec, WebPCodec
from hub.codec import BaseImgCodec, BaseNumCodec

compression_map = {
    PngCodec().__name__: PngCodec,
    JpegCodec().__name__: JpegCodec,
    WebPCodec().__name__: WebPCodec,
    Lz4().__name__: Lz4,
    Zstd().__name__: Zstd,
    NumPy().__name__: NumPy,
}


def _get_compressor(
    compressor_name: str, **kwargs
) -> Union[BaseImgCodec, BaseNumCodec]:
    """Get compressor object

    Example:
        compressor = _get_compressor('lz4', acceleration=2)

    Args:
        compressor_name (str): lowercase name of the required compressor
        **kwargs: Optional;
            acceleration (int): Lz4 codec argument. The larger the acceleration value,
            the faster the algorithm, but also the lesser the compression.
            level (int): Zstd codec argument. Sets the compression level (1-22).
            single_channel (bool): PngCodec and JpegCodec argument. if True,
            encoder will remove the last dimension of input if it is 1.
            Doesn't have impact on 3-channel images.
            quality (int): JpegCodec argument. The image quality on a scale from 1 (worst) to 95 (best).

    Returns:
        Codec object providing compression

    Raises:
        ValueError: if the name of compressor isn't in ['lz4', 'zstd', 'numpy', 'png', 'jpeg']
    """
    compressor = compression_map.get(compressor_name, None)
    if compressor:
        return compressor(**kwargs)
    else:
        raise ValueError(
            f"Wrong compressor: {compressor}"
            " only 'lz4', 'png', 'jpeg', 'numpy', 'zstd' and 'webp' are supported."
        )
