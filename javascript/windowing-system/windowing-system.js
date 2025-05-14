// @ts-check

/**
 * Implement the classes etc. that are needed to solve the
 * exercise in this file. Do not forget to export the entities
 * you defined so they are available for the tests.
 */

export function Size(width = 80, height = 60) {
  this.resize(width, height)
}

Size.prototype.resize = function (width, height) {
  this.width = width
  this.height = height
}

export function Position(x = 0, y = 0) {
  this.move(x, y)
}

Position.prototype.move = function (newX, newY) {
  this.x = newX
  this.y = newY
}

export class ProgramWindow {
  constructor() {
    this.screenSize = new Size(800, 600)
    this.size = new Size()
    this.position = new Position()
  }

  resize(size) {
    const maxW = this.screenSize.width - this.position.x
    const maxH = this.screenSize.height - this.position.y
    this.size.resize(
      Math.max(1, Math.min(maxW, size.width)),
      Math.max(1, Math.min(maxH, size.height))
    )
  }

  move(position) {
    const maxX = this.screenSize.width - this.size.width
    const maxY = this.screenSize.height - this.size.height
    this.position.move(
      Math.max(0, Math.min(maxX, position.x)),
      Math.max(0, Math.min(maxY, position.y))
    )
  }
}

export function changeWindow(window) {
  window.size.resize(400, 300)
  window.position.move(100, 150)
  return window
}
