import argparse
import os
import eulerian_magnification as em


def main(args):
    print(dir(em))
    all_paths = os.listdir(args.input_dir)
    for vid_path in all_paths:
        vid, fps = em.load_video_float(vid_path)
        em.eulerian_magnification(vid, fps,
                                      freq_min=50.0 / 60.0,
                                      freq_max=1.0,
                                      amplification=50,
                                      pyramid_levels=3)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="eulerian magnification")
    parser.add_argument('--input_dir', type=str, default='/home/shruti/deepfake-thesis/data/eulerian_mrub',
                        help='directory containing videos to be magnified')
    args = parser.parse_args()
    main(args)
