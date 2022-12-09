const {rgbToHexColor} = require('./rgbToHex');
const {expect} = require('chai');

describe('RGB to Hex tests', () => {
    it('black color', () => {
        expect(rgbToHexColor(0, 0, 0)).to.equal('#000000');
    });

    it('white color', () => {
        expect(rgbToHexColor(255, 255, 255)).to.equal('#FFFFFF');
    });

    it('blue color', () => {
        expect(rgbToHexColor(35, 68, 101)).to.equal('#234465');
    });

    it('return undefined', () => {
        expect(rgbToHexColor(0, 0)).to.be.undefined;
        expect(rgbToHexColor(0)).to.be.undefined;
        expect(rgbToHexColor()).to.be.undefined;
    });

    it('undefined for lower bound', () => {
        expect(rgbToHexColor(-1, 0, 0)).to.be.undefined;
        expect(rgbToHexColor(0, -1, 0)).to.be.undefined;
        expect(rgbToHexColor(0, 0, -1)).to.be.undefined;
    });

    it('undefined for upper bound', () => {
        expect(rgbToHexColor(256, 0, 0)).to.be.undefined;
        expect(rgbToHexColor(0, 256, 0)).to.be.undefined;
        expect(rgbToHexColor(0, 0, 256)).to.be.undefined;
    });

    it('floats', () => {
        expect(rgbToHexColor(1.1, 0, 0)).to.be.undefined;
        expect(rgbToHexColor(0, 1.1, 0)).to.be.undefined;
        expect(rgbToHexColor(0, 0, 1.1)).to.be.undefined;
    });

    it('converts 15 15 15 15', () => {
        expect(rgbToHexColor(15, 15, 15)).to.equal('#0F0F0F');
    });

});



